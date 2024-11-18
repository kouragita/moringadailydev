from flask_restful import Resource
from flask import request
from app.models import db, Category
from app.schemas import CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

class CategoryListResource(Resource):
    def get(self):
        categories = Category.query.all()
        return categories_schema.dump(categories), 200
    
    def post(self):
        data = request.get_json()
        category = category_schema.load(data)
        db.session.add(category)
        db.session.commit()
        return category_schema.dump(category), 201

class CategoryResource(Resource):
    def get(self, category_id):
        category = Category.query.get_or_404(category_id)
        return category_schema.dump(category), 200
    
    def delete(self, category_id):
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        return {"message": "Category deleted successfully."}, 200
