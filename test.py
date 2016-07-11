from flask import Flask
from flask_nemo import Nemo
from flask_nemo.chunker import level_grouper
from MyCapytain.common.reference import URN

from perseus_nemo_ui import PerseusNemoUi
from pkg_resources import resource_filename

app = Flask("Nemo")
app.debug = True
nemo = Nemo(
    app=app,
    base_url="",
    api_url="http://cts.perseids.org/api/cts",
    chunker={"default": level_grouper},
    plugins=[PerseusNemoUi()],
    transform={"default": resource_filename("perseus_nemo_ui","data/assets/static/xslt/epidocShort.xsl")}
)

app.run()
