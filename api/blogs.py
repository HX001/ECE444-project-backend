from flask import Response, request, jsonify
from flask_restful import Resource
from Blogs.blog_model import Blogs

# function to fetch all info of articles stored in db
class GetBlogsInfo(Resource):
    @staticmethod
    def post() -> Response:
        body = request.get_json()
        username = body['username']

        return jsonify(Blogs.objects)

# create new articles
class CreateNewArticle(Resource):
    @staticmethod
    def post() -> Response:
        body = request.get_json()
        username = body['username']
        title = body['title']
        content = body['content']
        imageurl = body["imageURL"]
        rating = body["rating"]

        # error checking
        article_exist = Blogs.objects(username=username, title=title).first()
        if article_exist is not None:  # check if this article already exists
            return jsonify({"status": 'fail', "message": "Article already exists"})

        # save article's info in db
        # new_article = Blogs(username=username, title=title, content=content)
        new_article = Blogs(username=username, title=title, content=content, imageURL=imageurl, rating=rating)
        new_article.save()
        return jsonify({"status": 'success', "message": "Successfully created article"})

# return an article's information given the id
class GetArticleById(Resource):
    @staticmethod
    def post() -> Response:

        body = request.get_json()
        title = body['title']

        # error handling
        # check if the article exists in the db
        try:
            article = Blogs.objects(title=title).first()
        except:
            return jsonify({"status": 'fail', "message": "Article does not exist"})
        return article.to_json()