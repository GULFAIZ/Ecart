const mysql = require('mysql2');

const pool = mysql.createPool({
  host: 'localhost',
  user: 'your_mysql_user',
  password: 'your_mysql_password',
  database: 'your_database_name',
  waitForConnections: true,
  connectionLimit: 10,
});

module.exports = pool.promise();
