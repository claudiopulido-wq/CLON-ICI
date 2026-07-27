const chatHTML = `
<!-- ================= CHATBOT ================= -->
<button class="chat-fab" onclick="toggleChat()" aria-label="Abrir asistente ICI"><span class="ping"></span><i class="fa-solid fa-message"></i></button>
<div class="chat-panel" id="chatPanel">
  <div class="chat-head">
    <span class="dot-live"></span>
    <div><strong>Asistente ICI</strong><span>Responde con base en tus certificaciones · RAG</span></div>
  </div>
  <div class="chat-body" id="chatBody">
    <div class="msg bot">Hola 👋 soy el asistente de ICI. Puedo responder sobre temarios, precios, planes de pago y requisitos de cada certificación. ¿En qué te ayudo?</div>
  </div>
  <div class="chat-suggestions">
    <button onclick="chatAsk('¿Cuánto cuesta el certificado de Personal Trainer?')">Precios</button>
    <button onclick="chatAsk('¿Qué incluye el temario?')">Temario</button>
    <button onclick="chatAsk('¿Tiene validez internacional?')">Validez</button>
  </div>
  <div class="chat-input-row">
    <input id="chatInput" placeholder="Escribe tu pregunta..." onkeypress="if(event.key === 'Enter') chatSend()">
    <button onclick="chatSend()"><i class="fa-solid fa-paper-plane"></i></button>
  </div>
</div>
`;

document.body.insertAdjacentHTML('beforeend', chatHTML);

function toggleChat(){
    document.getElementById('chatPanel').classList.toggle('open');
}

function chatAsk(text){
    document.getElementById('chatInput').value=text; 
    chatSend();
}

function chatSend(){
  const input=document.getElementById('chatInput');
  const text=input.value.trim();
  if(!text) return;
  const body=document.getElementById('chatBody');
  body.insertAdjacentHTML('beforeend', `<div class="msg user">${text}</div>`);
  input.value='';
  body.scrollTop=body.scrollHeight;
  // TODO (Antigravity / backend): reemplazar este setTimeout por una llamada real
  // al servicio RAG (retrieval sobre temarios, precios, FAQs y políticas de ICI)
  setTimeout(()=>{
    body.insertAdjacentHTML('beforeend', `<div class="msg bot">Esta es una respuesta simulada. Aquí se conectará el motor RAG con la base de conocimiento real de ICI (temarios, precios, políticas y FAQs) para responder: "${text}"</div>`);
    body.scrollTop=body.scrollHeight;
  }, 500);
}
