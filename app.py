from flask import Flask, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)

