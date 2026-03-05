<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prezi Clone - ZUI</title>
    <style>
        body, html { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background: #f0f0f0; font-family: sans-serif; }
        #viewport { position: relative; width: 100vw; height: 100vh; overflow: hidden; }
        /* O canvas é onde todos os objetos são colocados; a transição suave cria o efeito Prezi */
        #canvas { position: absolute; transform-origin: 0 0; transition: transform 1.5s cubic-bezier(0.45, 0, 0.55, 1); }
        .object { position: absolute; white-space: nowrap; font-size: 24px; }
        .frame { border: 2px solid #007bff; background: rgba(0, 123, 255, 0.05); width: 400px; height: 300px; }
        #controls { position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 100; display: flex; gap: 10px; }
        button { padding: 10px 20px; cursor: pointer; background: #007bff; color: white; border: none; border-radius: 5px; font-weight: bold; }
    </style>
</head>
<body>
    <div id="viewport">
        <div id="canvas"></div>
    </div>
    <div id="controls">
        <button onclick="prev()">Anterior</button>
        <button onclick="next()">Próximo</button>
    </div>
    <script>
        let currentStep = 0;
        let objects = [];
        const canvas = document.getElementById('canvas');

        // Carrega os dados da API do Flask
        async function loadPresentation() {
            try {
                const response = await fetch('/api/get_presentation');
                const data = await response.json();
                objects = data.objects;
                render();
                updateView();
            } catch (e) { console.error(e); }
        }

        // Renderiza os objetos no canvas
        function render() {
            canvas.innerHTML = '';
            objects.forEach(obj => {
                const el = document.createElement('div');
                el.className = 'object ' + (obj.type === 'frame' ? 'frame' : '');
                el.innerText = obj.type === 'text' ? obj.content : '';
                el.style.left = obj.x + 'px';
                el.style.top = obj.y + 'px';
                el.style.transform = `scale(${obj.scale}) rotate(${obj.rotation}deg)`;
                canvas.appendChild(el);
            });
        }

        // Calcula a transformação necessária para centralizar e dar zoom no objeto atual
        function updateView() {
            if (objects.length === 0) return;
            const target = objects[currentStep];
            const vw = window.innerWidth;
            const vh = window.innerHeight;
            
            const scale = 1 / target.scale;
            const tx = (vw / 2) - (target.x * scale);
            const ty = (vh / 2) - (target.y * scale);
            
            canvas.style.transform = `translate(${tx}px, ${ty}px) scale(${scale})`;
        }

        function next() {
            currentStep = (currentStep + 1) % objects.length;
            updateView();
        }

        function prev() {
            currentStep = (currentStep - 1 + objects.length) % objects.length;
            updateView();
        }

        loadPresentation();
        // Ajusta a visualização se a janela for redimensionada
        window.addEventListener('resize', updateView);
    </script>
</body>
</html>
