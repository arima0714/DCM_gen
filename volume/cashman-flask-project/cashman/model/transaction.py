import datetime as dt

from mashmallow import Schema, fields

class Transaction():
    def __inint__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def__repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self-self)

class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()
