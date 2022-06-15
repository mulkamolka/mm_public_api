--- 소매시장 테이블 생성
CREATE TABLE market_retail(
m_code VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '상점코드',
m_name VARCHAR(45) NOT NULL COMMENT '상점명',
m_type INT NOT NULL COMMENT '상점타입',
loc POINT NULL COMMENT '좌표'
) ENGINE=InnoDB
COMMENT '소매점정보';

--- 도매시장 테이블
CREATE TABLE market_wholesale(
m_code VARCHAR(20) NOT NULL PRIMARY KEY COMMENT '상점코드',
m_origin VARCHAR(50) NULL COMMENT '원산지'
) ENGINE=InnoDB
COMMENT '도매정보';

--- 상품 테이블

CREATE TABLE product(
p_code VARCHAR(25) NOT NULL PRIMARY KEY COMMENT '상품코드',
p_name VARCHAR(100) NOT NULL COMMENT '상품명',
category INT UNSIGNED COMMENT '카테고리',
m_code_r VARCHAR(20) NULL COMMENT '소매상점코드',
m_code_w VARCHAR(20) NULL COMMENT '도매상점코드',
key fk_mr (m_code_r),
key fk_mw (m_code_w),
CONSTRAINT fk_mr FOREIGN KEY (m_code_r) REFERENCES market_retail(m_code) ON DELETE NO ACTION ON UPDATE NO ACTION,
CONSTRAINT fk_mw FOREIGN KEY (m_code_w) REFERENCES market_wholesale(m_code) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB
COMMENT '상품정보';

---- 가격 테이블
CREATE TABLE price(
date VARCHAR(30) NOT NULL COMMENT '등록날짜',
p_code VARCHAR(45) NOT NULL COMMENT '상점명',
price DECIMAL NOT NULL COMMENT '가격',
primary key(date,p_code),
key fk_p_code (p_code),
CONSTRAINT fk_p_code FOREIGN KEY (p_code) REFERENCES product(p_code) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB
COMMENT '가격';

--- 농산물 소매 테이블
CREATE TABLE agriproduct_retail(
p_code VARCHAR(25) NOT NULL PRIMARY KEY COMMENT '상품코드',
p_group VARCHAR(50) NOT NULL COMMENT '상품군',
category INT UNSIGNED COMMENT '카테고리',
unit VARCHAR(30) COMMENT '단위',
description VARCHAR(100) NULL COMMENT '비고',
key fk_p_code_ag_r (p_code),
CONSTRAINT fk_p_code_ag_r FOREIGN KEY (p_code) REFERENCES product(p_code) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB
COMMENT '농산물소매';