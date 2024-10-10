class AutomobileCompany:
    company_name = ""
    headquarters = ""

    @classmethod
    def get_info(cls):
        return f"Company: {cls.company_name}, Headquarters: {cls.headquarters}"
    
    @classmethod
    def operations(cls):
        return "Operations not defined for this company."

class PorscheAG(AutomobileCompany):
    company_name = "Porsche AG"
    headquarters = "Stuttgart, Germany"
    models = ["911", "Cayenne", "Taycan"]

    @classmethod
    def operations(cls):
        return f"{cls.company_name} specializes in luxury sports cars like {', '.join(cls.models)}."

class VWGroup(AutomobileCompany):
    company_name = "Volkswagen Group"
    headquarters = "Wolfsburg, Germany"
    brands = ["Audi", "Bentley", "Porsche AG", "Volkswagen"]

    @classmethod
    def operations(cls):
        return f"{cls.company_name} manages multiple brands like {', '.join(cls.brands)}."

class PorscheSE(AutomobileCompany):
    company_name = "Porsche SE"
    headquarters = "Stuttgart, Germany"
    controlled_stake = 53.3

    @classmethod
    def operations(cls):
        return f"{cls.company_name} owns a controlling {cls.controlled_stake}% stake in Volkswagen Group."

companies = [PorscheSE, VWGroup, PorscheAG]

for company in companies:
    print(company.get_info())
    print(company.operations())
    print("-" * 85)
