class Error(Exception):
    """klasa bazowa dla wyjątków"""
    pass


class PrzepelnienieDrobnych(Error):
    message = "Parkomat przepelniony, prosze placic bankontami"


class RejestracjaMaleLitery(Error):
    message = "rejestracja moze skladac sie jedynie z duzych liter\nwprowadz nr rejetracji samochodu jeszcze raz"


class NieWprowadzonoNrR(Error):
    message = "wprowadz numer rejestracyjny"


class NieWrzuconoMonet(Error):
    message = "Nie wrzucono zadnej monety"
