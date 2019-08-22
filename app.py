#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 20, 2019


Flask APP configuration
"""
import connexion

app = connexion.FlaskApp(__name__)
app.add_api('swagger.yml')

if __name__ == '__main__':
    app.run(port=8080)
