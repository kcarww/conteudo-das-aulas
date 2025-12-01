CREATE DATABASE IF NOT EXISTS sistema_estoque;
USE sistema_estoque;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) DEFAULT 'operador',
    ativo BOOLEAN DEFAULT TRUE,
    data_cadastro DATETIME DEFAULT now()
);


CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT
);



CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    codigo_barras VARCHAR(50) UNIQUE,
    categoria_id INT,
    preco_compra DECIMAL(10, 2),
    preco_venda DECIMAL(10, 2),
    estoque_minimo INT DEFAULT 0,
    estoque_atual INT DEFAULT 0,
    unidade_medida VARCHAR(20) DEFAULT 'UN', 
    ativo BOOLEAN DEFAULT TRUE,
    data_cadastro DATETIME DEFAULT now(),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE movimentacoes_estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    usuario_id INT NOT NULL,
    tipo ENUM('ENTRADA', 'SAIDA') NOT NULL,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10, 2),
    valor_total DECIMAL(10, 2),
    data_movimentacao DATETIME DEFAULT now(),
    observacao TEXT,
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


INSERT INTO categorias (nome, descricao) VALUES
('Eletrônicos', 'Produtos eletrônicos e tecnologia'),
('Alimentos', 'Produtos alimentícios'),
('Limpeza', 'Produtos de limpeza'),
('Escritório', 'Material de escritório');


INSERT INTO usuarios (nome, email, senha, tipo) VALUES
('Administrador', 'admin@sistema.com', 'admin123', 'admin');

