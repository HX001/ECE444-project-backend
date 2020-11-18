from flask import Response, request, jsonify
from flask_restful import Resource
from Recipes.recipe_model import Recipe
from Users.user_model import Users


class SaveARecipe(Resource):
    @staticmethod
    def post() -> Response:
        body = request.get_json()
        username = body['username']
        label = body['label']
        url = body['url']
        image = body['image']
        # Check if user exists
        user_exist = Users.objects(user_name=str(username)).first()
        if user_exist is None:
            return jsonify({"status": 'fail', "message": 'User does not exist'})
        # Check whether the user has already saved this recipe
        article_already_saved = Recipe.objects(username=str(username), label=str(label)).first()
        if article_already_saved:
            return jsonify({"status": 'fail', "message": 'Have saved this recipe'})
        # save recipe's info in db
        new_article = Recipe(username=str(username), label=str(label), url=str(url), image=str(image))
        new_article.save()
        return jsonify({"username": str(username), "label": str(label), "url": str(url), "image": str(image),
                        "status": 'success', "message": "Successfully Saved!"})


