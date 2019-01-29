create database account 
default charset = utf8;-- 创建account数据库

create table account(
    account varchar(32) primary key
    )default charset = utf8;-- 创建account表

insert into account -- 插入初始数据
values('1931784039@qq.com'),
    ('253862251@qq.com'),
    ('1194681498@qq.com');

alter table account modify account varchar(32)not null unique;

alter table account add ind int(4) unique;

insert into account -- 插入初始数据
values('1931784039@qq.com',1),
    ('253862251@qq.com',2),
    ('1194681498@qq.com',3);
