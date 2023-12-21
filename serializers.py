def serialize_contact(model):
    return {
        'id': model.id,
        'fcs': model.fcs,
        'phone': model.phone,
        'address': model.address
    }


def serialize_customer(model):
    return {
        'id': model.id,
        'contact': {
            'id': model.contact.id,
            'fcs': model.contact.fcs,
            'phone': model.contact.phone,
            'address': model.contact.address,
        },
        'completed_payments': model.completed_payments,
        'water_debt': model.water_debt,
        'internet_debt': model.internet_debt,
        'warm_debt': model.water_debt
    }


def serialize_issues(model):
    return {
        'id': model.id,
        'customer': {
            'id': model.customer.id,
            'contact': {
                'id': model.customer.contact.id,
                'fcs': model.customer.contact.fcs,
                'phone': model.customer.contact.phone,
                'address': model.customer.contact.address,
            },
            'completed_payments': model.customer.completed_payments,
            'water_debt': model.customer.water_debt,
            'internet_debt': model.customer.internet_debt,
            'warm_debt': model.customer.water_debt
        },
        'job': model.job,
        'contract': model.contract
    }


def serialize_executor(model):
    return {
        'id': model.id,
        'contact': {
            'id': model.contact.id,
            'fcs': model.contact.fcs,
            'phone': model.contact.phone,
            'address': model.contact.address,
        },
        'issues': {
            'id': model.issues.id,
            'customer': {
                'id': model.issues.customer.id,
                'contact': {
                    'id': model.issues.customer.contact.id,
                    'fcs': model.issues.customer.contact.fcs,
                    'phone': model.issues.customer.contact.phone,
                    'address': model.issues.customer.contact.address,
                },
                'completed_payments': model.issues.customer.completed_payments,
                'water_debt': model.issues.customer.water_debt,
                'internet_debt': model.issues.customer.internet_debt,
                'warm_debt': model.issues.customer.water_debt
            },
            'job': model.issues.job,
            'contract': model.issues.contract
        },
        'completed_works': model.completed_works,
        'rating': model.rating,
        'time_working': model.time_working
    }
