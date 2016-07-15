"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """docstring for AbstractMelonOrder"""
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price."""
        base_price = 5
        if self.species == "Christmas":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True
       

class GovernmentMelonOrder(AbstractMelonOrder):
    """docstring for GovernmentMelonOrder"""
    passed_inspection = False

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0.0)
        

    def mark_inspection(self):
        self.passed_inspection = True

        
class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty,'domestic', 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        self.country_code = country_code

        super(InternationalMelonOrder, self).__init__(species, qty, 'international', 0.17)

     

    def get_country_code(self):

        """Return the country code."""

        return self.country_code
