# coding: utf8
__author__ = 'JinXing'


from flask import request, render_template
from matrix import app
from matrix.models import db, Area, User, AreaMember


@app.route("/area/", endpoint="list_area")
def list_area():
    return request.method + u" AREA"


@app.route("/area/<area_name>", endpoint="area")
def show_area(area_name):
    area = Area.query.filter_by(short_name=area_name).first_or_404()
    area.creator = User.query.filter_by(id=area.creator).first_or_404()

    # area.member_num = AreaMember.query.count().filter_by(area=area.id) # fixme: 为什么运行报错？
    # area.members = AreaMember.query.join(AreaMember.members).filter_by(area=area.id)
    sql = "SELECT user.account,user.name FROM area_member,user" \
          " WHERE area_member.user = user.id and area_member.area = %d" % area.id
    area.members = db.session.execute(sql).fetchall()

    return render_template("show_area.html", area=area)
