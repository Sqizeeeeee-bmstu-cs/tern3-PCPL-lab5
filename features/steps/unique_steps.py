from behave import given, when, then

from myclass import Unique


def parse(text):
    return [s.strip() for s in text.split(',')] if text else []


@given('список значений "{text}"')
def step_given(context, text):
    context.items = parse(text)

@given('пустой список значений')
def step_given_empty(context):
    context.items = []

@when('я получаю уникальные значения с игнорированием регистра')
def step_when_ic(context):
    context.result = list(Unique(context.items, ignore_case=True))


@when('я получаю уникальные значения')
def step_when(context):
    context.result = list(Unique(context.items))


@then('результат равен "{text}"')
def step_then(context, text):
    assert context.result == parse(text)


@then('результат пустой')
def step_then_empty(context):
    assert context.result == []
