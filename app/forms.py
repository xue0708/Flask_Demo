# -*- coding: utf-8 -*-
import sys
import os

from wtforms.validators import ValidationError, Email, EqualTo
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

sys.path.append("..")
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


class LoginForm(FlaskForm):
	username = StringField('系统名', validators=[DataRequired(message='请输入系统名称')])
	password = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
	remember_me = BooleanField('记住此信息')
	submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
	username = StringField('系统名', validators=[DataRequired()])
	password = PasswordField('密码')
	password2 = PasswordField('确认密码', validators=[EqualTo('password')])
	submit = SubmitField('注册')
	#验证用户名是否被使用
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('此系统名已经被使用！')


class EditProfileForm(FlaskForm):
	username = StringField('输入新的系统名称', validators=[DataRequired(message='请输入系统名!')])
	submit = SubmitField('提交')


class CSVDownloadForm(FlaskForm):
    number = StringField('输入组数', validators=[DataRequired(message='请输入组数!')])
    startTime = StringField('输入开始时间', validators=[DataRequired(message='请输入开始时间!')])
    endTime = StringField('输入结束时间', validators=[DataRequired(message='请输入结束时间!')])
    submit = SubmitField('确定')


class SetMaxNumForm(FlaskForm):
	maxdx = StringField('输入最大dx阈值', validators=[DataRequired(message='请输入阈值!')])
	maxdy = StringField('输入最大dy阈值', validators=[DataRequired(message='请输入阈值!')])
	maxdz = StringField('输入最大dz阈值', validators=[DataRequired(message='请输入阈值!')])
	maxgx = StringField('输入最大gx阈值', validators=[DataRequired(message='请输入阈值!')])
	maxgy = StringField('输入最大gy阈值', validators=[DataRequired(message='请输入阈值!')])
	maxgz = StringField('输入最大gz阈值', validators=[DataRequired(message='请输入阈值!')])
	submit = SubmitField('提交')
