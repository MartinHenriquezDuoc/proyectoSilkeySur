// server.js
const express = require('express');
const MercadoPago = require('mercadopago');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

MercadoPago.configure({
    access_token: 'TEST-710084918786297-052121-2c27e4166653e3ca3b0ccf576414df7a-363340795'
});

app.post('/create_preference', (req, res) => {
    let preference = {
        items: [
            {
                title: 'Mi producto',
                unit_price: 100,
                quantity: 1,
            }
        ]
    };

    MercadoPago.preferences.create(preference)
        .then(response => {
            res.json({ id: response.body.id });
        }).catch(error => {
            console.log(error);
            res.status(500).send('Error al crear la preferencia');
        });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
