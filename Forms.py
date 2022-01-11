from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
import hashlib
#from wtforms.fields.html5 import EmailField, DateField
from wtforms import EmailField, DateField

# class CreateUserForm(Form):    #CreateUserForm inherits from class Form
#     first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
#     membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
#     remarks = TextAreaField('Remarks', [validators.Optional()])
#
# class CreateCustomerForm(Form):
#     first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
#     email = EmailField('Email', [validators.Email(), validators.DataRequired()])
#     date_joined = DateField('Date Joined', format='%Y-%m-%d')
#     address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
#     membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
#     remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateCustomerForm(Form):
      first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
      last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
      mobile_no = StringField('Mobile Number', [validators.Length(min=1, max=150), validators.DataRequired()])#unsolved
      address = TextAreaField('Address', [validators.length(max=200), validators.DataRequired()])
      username = StringField('Username', [validators.Length(min=1, max=15), validators.DataRequired()])
      # password = hashlib.md5('Password')
      password= StringField('Password', [validators.Length(min=1, max=15), validators.DataRequired()])

class LoginCustomerForm(Form):

      username = StringField('Username', [validators.Length(min=1, max=15), validators.DataRequired()])
      # password = hashlib.md5('Password')
      password= StringField('Password', [validators.Length(min=1, max=15), validators.DataRequired()])


class CreateSupportForm(Form):

      def __init__(
              self,
              formdata=None,
              obj=None,
              prefix="",
              data=None,
              meta=None,
              **kwargs,
      ):
            super().__init__(formdata, obj, prefix, data, meta, kwargs)
            self.order_id = None

      name = StringField('Name', [validators.Length(min=1, max=50), validators.DataRequired()])
      email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
      outlet = StringField('Outlet ordered from', [validators.Length(min=1, max=50), validators.Optional()])
      platform = StringField('Platform ordered from', [validators.length(min=1, max=50), validators.Optional()])
      id = StringField('Order ID', [validators.Length(min=1, max=15), validators.Optional()])
      subject= StringField('Subject', [validators.Length(min=1, max=15), validators.DataRequired()])
      enquiry= TextAreaField('Enquiry', [validators.Length(max=1000), validators.DataRequired()])
