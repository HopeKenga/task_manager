from flask import Flask
from prisma import PrismaClient

app = Flask(__name__)

prisma = PrismaClient()
app.prisma = PrismaClient


