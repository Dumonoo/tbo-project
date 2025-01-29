from project import db, app
import bleach
import logging

logging.basicConfig(level=logging.ERROR, filename="validation_errors.log")

def log_error(message):
    logging.error(message)

# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pesel = db.Column(db.String(11), nullable=False)
    street = db.Column(db.String(128), nullable=False)
    appNo = db.Column(db.String(10), nullable=False)

    @staticmethod
    def is_sql_injection(value):
        sql_keywords = [
            "SELECT", "INSERT", "DELETE", "UPDATE", "DROP", "--", ";", "' OR", "' AND", "'=",
            "UNION", "EXEC", "SHUTDOWN", "XP_"
        ]
        return any(keyword in value.upper() for keyword in sql_keywords)

    @staticmethod
    def sanitize_input(value):
        return bleach.clean(value, tags=[], attributes={}, strip=True)


    @staticmethod
    def contains_malicious_content(value):
        """
        Checks for XSS-like patterns in the input.
        """
        xss_patterns = [
            "<script>",
            "</script>",
            "javascript:",
            "onerror=",
            "onclick=",
            "<iframe>",
        ]
        value_lower = value.lower()
        return any(pattern in value_lower for pattern in xss_patterns)

    def __init__(self, name, city, age, pesel, street, appNo):
        try:
            if not name or len(name.strip()) == 0:
                raise ValueError("Customer name cannot be empty")
            if self.is_sql_injection(name):
                raise ValueError("Potential SQL injection detected in name")
            if self.contains_malicious_content(name):
                raise ValueError("Potential XSS detected in name")

            if not city or len(city.strip()) == 0:
                raise ValueError("City cannot be empty")
            if self.is_sql_injection(city):
                raise ValueError("Potential SQL injection detected in city")
            if self.contains_malicious_content(city):
                raise ValueError("Potential XSS detected in city")

            if age <= 0:
                raise ValueError("Age must be a positive integer")
            if not pesel.isdigit() or len(pesel) != 11:
                raise ValueError("Pesel must be an 11-digit number")
            if not street or len(street.strip()) == 0:
                raise ValueError("Street cannot be empty")
            if self.is_sql_injection(street):
                raise ValueError("Potential SQL injection detected in street")
            if self.contains_malicious_content(street):
                raise ValueError("Potential XSS detected in street")

            if len(appNo) > 10:
                raise ValueError("AppNo must not exceed 10 characters")

            # Sanitize inputs
            self.name = name
            self.city = self.sanitize_input(city)
            self.street = self.sanitize_input(street)
            self.age = age
            self.pesel = pesel
            self.appNo = appNo
        except ValueError as e:
            logging.error(f"Validation error: {str(e)}")
            raise

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {mask_data(self.city, 1)}, Age: {self.age}, Pesel: {mask_data(self.pesel)}, Street: {mask_data(self.street, 1)}, AppNo: {mask_data(self.appNo)})"

def mask_data(data, visible_start=0, mask_char="*", mask_length=None):
    if isinstance(data, int):
        data_str = str(data)
        mask_length = mask_length or len(data_str) - visible_start
        return data_str[:visible_start] + (mask_char * mask_length)
    elif isinstance(data, str):
        masked_length = mask_length or max(0, len(data) - visible_start)
        return data[:visible_start] + (mask_char * masked_length)
    return mask_char * 8  # Default mask for unknown types


with app.app_context():
    db.create_all()
