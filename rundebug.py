#!/usr/bin/env python2
from matrix import app
import sys


if len(sys.argv) < 2:
    app.run(debug=True, host='0.0.0.0', port=8080)
    sys.exit(1)

command = sys.argv[1]
if command == "init-db":
    print "init databases ..."
    from matrix import models
    models.db.create_all()
elif command == "drop-db":
    print "drop databases ..."
    from matrix import models
    models.db.drop_all()

