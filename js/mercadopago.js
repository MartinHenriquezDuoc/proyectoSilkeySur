// mercadopago.js
const mp = new MercadoPago('TEST-b2c13c98-3097-41ec-a01f-028841d4a158', {
    locale: 'es-CL'
});

document.getElementById('checkout-button').addEventListener('click', async () => {
    // Llamar a tu backend para crear una preferencia de pago y obtener el ID
    const response = await fetch('/create_preference', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const preference = await response.json();

    mp.checkout({
        preference: {
            id: preference.id
        },
        render: {
            container: '#checkout', // Indica dónde se mostrará el botón de Mercado Pago
            label: 'Pagar', // Cambia el texto del botón
        }
    });
});
