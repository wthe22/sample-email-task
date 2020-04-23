
from src import main


app = main()
app.debug = True
app.run(host='0.0.0.0')
