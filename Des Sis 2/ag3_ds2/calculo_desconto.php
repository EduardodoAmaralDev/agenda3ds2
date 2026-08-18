<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $nome = $_POST["txtNome"];
    $valorCompra = $_POST["txtValorCompra"];
    $formaPagamento = $_POST["cmbPag"];
    $desconto = 0;

    // Cálculo do desconto
    if ($formaPagamento == "cartaoCredito") {

        $desconto = 0;
        $mensagem = "Olá $nome, sua compra de R$ $valorCompra foi realizada com cartão de crédito. Não há desconto.";

    } elseif ($formaPagamento == "boleto") {

        $desconto = $valorCompra * 0.08;
        $mensagem = "Olá $nome, sua compra de R$ $valorCompra foi realizada com boleto. Seu desconto é de R$ $desconto.";

    } elseif ($formaPagamento == "deposito") {

        $desconto = $valorCompra * 0.10;
        $mensagem = "Olá $nome, sua compra de R$ $valorCompra foi realizada com depósito. Seu desconto é de R$ $desconto.";

    } else {

        $mensagem = "Forma de pagamento inválida.";
    }

    echo "
    <!DOCTYPE html>
    <html lang='pt-BR'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>
        <title>Cálculo do Desconto</title>
    </head>

    <body>
        <div class='w3-container w3-teal w3-center w3-padding-16'>
            <h2>Desconto concedido</h2>
        </div><br>
        <div class='w3-container' style='max-width:600px; margin:auto;'>
            <div class='w3-card-4 w3-padding w3-light-grey'>
                <div class='w3-panel w3-green w3-round'>
                    <p>$mensagem</p>
                </div>

                <div class='w3-center'>
                    <a href='form_calculo_desc.html'><button class='w3-button w3-teal w3-hover-green w3-round'> Voltar ao Formulário </button></a>
                </div>
            </div>
        </div>

    </body>
    </html>
    ";
}
?>