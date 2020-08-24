from behave import then, when

@when('somar "{num_1:d}" e "{num_2:d}"')
def soma_dois_valores(context, num_1, num_2):
    pass


@then('o resultado deve ser "{result:d}"')
def assert_result(context, result):
    pass

