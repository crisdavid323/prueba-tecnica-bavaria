from colorama import init, Fore

init()


class Validate:
    def __init__(self, fields_completed):
        self.fields_completed = fields_completed

    def showValidate(self):
        for campo, estado in self.fields_completed.items():
            if estado:
                print(f"El campo {campo} {Fore.GREEN}pasó{Fore.RESET} la validación.")
            else:
                print(f"El campo {campo} {Fore.RED}no pasó{Fore.RESET} la validación.")
