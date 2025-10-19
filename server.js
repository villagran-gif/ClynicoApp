const express = require('express');
const app = express();
const PORT = process.env.PORT || 8080;

// sirve contenido estático construido en /dist
app.use(express.static('dist'));

// endpoint simple para healthcheck
app.get('/_ah/warmup', (req, res) => res.send('ok'));
app.get('/healthz', (req, res) => res.send('ok'));

app.listen(PORT, '0.0.0.0', () => {
  console.log('ClynicoApp server listening on', PORT);
});
