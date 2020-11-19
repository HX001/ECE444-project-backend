# flask packages
from flask_restful import Api
# project resources
from api.authentication import LoginApi, SignUpApi
from api.blogs import GetBlogsInfo, CreateNewArticle, GetArticleById
from api.recipes import SaveARecipe


def routes_creator(api: Api):
    api.add_resource(LoginApi, '/users/login')
    api.add_resource(SignUpApi, '/users/register')
    api.add_resource(GetBlogsInfo, '/blogs/')
    api.add_resource(CreateNewArticle, '/create/')
    api.add_resource(GetArticleById, '/articles/')
    api.add_resource(SaveARecipe, '/recipes/saveRecipe')