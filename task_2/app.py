import os

from flask import Flask, render_template, request
from flask_paginate import Pagination

from src.db_client import DB_Client

app = Flask(
    __name__,
    static_url_path="",
    static_folder='web/static',
    template_folder='web/templates'
)

db_client = DB_Client()


@app.route('/')
def main_page():
    age = request.args.get('age')
    breed = request.args.get('breed')
    page = int(request.args.get('page', 1))

    images = list(db_client.get_cats(age, breed))

    per_page = 5

    offset = (page - 1) * per_page

    total = len(images)
    pagination_images = images[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template(
        'main_page.html',
        images=pagination_images,
        page=page,
        per_page=per_page,
        pagination=pagination,
    )


@app.route('/profile')
def profile():
    name = request.args.get('name')
    cat = db_client.get_cat_by_name(name)
    return render_template(
        'profile.html',
        image=cat.img_path,
        name=cat.nickname,
        age=cat.age,
        breed=cat.breed,
        description=cat.description,
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=False, port=port)
