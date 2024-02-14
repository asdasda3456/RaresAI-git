from datetime import datetime

class DateHelper:
    @staticmethod
    def get_current_date():
        """
        Get the current date in the format YYYY-MM-DD.
        """
        current_date = datetime.now()
        return current_date.strftime("%Y-%m-%d")
