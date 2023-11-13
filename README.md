<head>
    <style>
       <link rel="stylesheet" type="text/css" href="./style-candidato.css" />
      </style>
  </head>
  <body>
      <div id="corpo">
         <img src="itapevi\teco.jpeg">
          <div id="texto">
              <div id ="n_local">CEMEB JORNALISTA JOÃO VALÉRIO DE PAULA NETO (ANTIGA EM MUNDO MAGICO)</div>
             <div id="button"> <button onclick="alterarVotos('$[votos_total/total_votos_20]');alterarano('2020')" size =>2020</button>  
    <button onclick="alterarVotos('$[votos_total/total_votos_16]');alterarano('2016')">2016</button>
    <button id = 'a2012' onclick="alterarVotos('$[votos_total/total_votos_12]');alterarano('2012')">2012</button></div>
              <div id="endereco">Endereço: $[votos_total/ENDERECO_LOCAL]</div>
              <div id="qnt_votos">Total de votos: <span id="votos"></span></div>
          </div>
          </div>

          <script>
            function alterarVotos(valor) {
                document.getElementById("votos").innerHTML = valor;
            }
    
            function alterarano(ano) {
                document.getElementById("ano").innerHTML = ano;
            }
        </script>
  </body>
