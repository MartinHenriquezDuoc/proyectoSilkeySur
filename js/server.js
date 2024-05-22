const express = require('express');
const bodyParser = require('body-parser');
const mercadopago = require('mercadopago');

mercadopago.configurations.setAccessToken('TEST-710084918786297-052121-2c27e4166653e3ca3b0ccf576414df7a-363340795');

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/create_preference', (req, res) => {
    let preference = {
        items: req.body.items,
        
        auto_return: 'approved',
    };

    mercadopago.preferences.create(preference)
        .then(function(response){
            res.json({ id: response.body.id });
        }).catch(function(error){
            console.log(error);
            res.status(500).send('Error al crear la preferencia');
        });
});

app.listen(3000, () => {
    console.log('Servidor escuchando en el puerto 3000');
});

