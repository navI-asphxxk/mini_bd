from models import Contact, Customer, Issues, Executor


def add_data():
    contact1 = Contact.create(id=1, fcs="Наметченко М А", phone="89092004433", address="ADR1")
    contact2 = Contact.create(id=2, fcs="Иванов А А", phone="89000000000", address="ADR2")
    contact3 = Contact.create(id=3, fcs="Петров Д Д", phone="89999999999", address="ADR3")
    contact4 = Contact.create(id=4, fcs="Минько С А", phone="89092000000", address="ADR4")
    contact5 = Contact.create(id=5, fcs="Меньшуткина Е А", phone="89103686949", address="ADR5")

    contact6 = Contact.create(id=6, fcs="Сидоров Е Е", phone="89092222233", address="ADR6")
    contact7 = Contact.create(id=7, fcs="Павлов И И", phone="89000000111", address="ADR7")
    contact8 = Contact.create(id=8, fcs="ФИО8", phone="89999995555", address="ADR8")
    contact9 = Contact.create(id=9, fcs="ФИО9", phone="89092008888", address="ADR9")
    contact10 = Contact.create(id=10, fcs="ФИО10", phone="89103680000", address="ADR10")

    customer1 = Customer.create(id=1, contact=contact1, water_debt=1000)
    customer2 = Customer.create(id=2, contact=contact2, internet_debt=1050)
    customer3 = Customer.create(id=3, contact=contact3, warm_debt=100)
    customer4 = Customer.create(id=4, contact=contact4, water_debt=1000, internet_debt=1000, warm_debt=1000)
    customer5 = Customer.create(id=5, contact=contact5)

    issue1 = Issues.create(id=1, customer=customer1, job="water")
    issue2 = Issues.create(id=2, customer=customer2, job="clean", contact="after work")
    issue3 = Issues.create(id=3, customer=customer3, job="warm")
    issue4 = Issues.create(id=4, customer=customer4, job="internet")
    issue5 = Issues.create(id=5, customer=customer5, job="warm, internet")

    executor1 = Executor.create(id=1, contact=contact6, issues=issue1, completed_works="Water", rating=100,
                                time_working=2)
    executor2 = Executor.create(id=2, contact=contact7, issues=issue2, time_working=10)
    executor3 = Executor.create(id=3, contact=contact8, issues=issue3, time_working=5)
    executor4 = Executor.create(id=4, contact=contact9, issues=issue4)
    executor5 = Executor.create(id=5, contact=contact10, issues=issue5)
