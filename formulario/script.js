function adicionarNaTabela() {
  // Pegar os valores do formulário
  var nome = document.getElementById('nome').value;
  var idade = document.getElementById('idade').value;
  var email = document.getElementById('email').value;
  var profissao = document.getElementById('profissao').value;
  var telefone = document.getElementById('telefone').value;

  // Validar se todos os campos estão preenchidos
  if (!nome || !idade || !email || !profissao || !telefone) {
    alert('Por favor, preencha todos os campos.');
    return;
  }

  // Acessar a tabela e o corpo dela
  var tabela = document.getElementById('tabela').querySelector('tbody');

  // Criar uma nova linha
  var novaLinha = document.createElement('tr');

  // Criar as células para cada dado
  var celulaNome = document.createElement('td');
  celulaNome.textContent = nome;

  var celulaIdade = document.createElement('td');
  celulaIdade.textContent = idade;

  var celulaEmail = document.createElement('td');
  celulaEmail.textContent = email;

  var celulaProfissao = document.createElement('td');
  celulaProfissao.textContent = profissao;

  var celulaTelefone = document.createElement('td');
  celulaTelefone.textContent = telefone;

  // Adicionar as células à linha
  novaLinha.appendChild(celulaNome);
  novaLinha.appendChild(celulaIdade);
  novaLinha.appendChild(celulaEmail);
  novaLinha.appendChild(celulaProfissao);
  novaLinha.appendChild(celulaTelefone);

  // Adicionar a linha à tabela
  tabela.appendChild(novaLinha);

  // Limpar os campos do formulário
  document.getElementById('formulario').reset();
}
