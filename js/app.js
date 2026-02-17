// NES Game Station - Main Application
class NESGameStation {
    constructor() {
        this.games = gamesDatabase;
        this.favorites = JSON.parse(localStorage.getItem('nes_favorites')) || [];
        this.recentlyPlayed = JSON.parse(localStorage.getItem('nes_recent')) || [];
        this.currentFilter = 'all';
        this.currentGame = null;
        this.nesEmulator = null;
        this.isPaused = false;
        this.isMuted = false;

        this.init();
    }

    init() {
        this.renderGames(this.games);
        this.setupEventListeners();
        this.updateStats();
        this.loadFromStorage();
    }

    // Render game cards
    renderGames(gamesToRender) {
        const gameGrid = document.getElementById('gameGrid');
        gameGrid.innerHTML = '';

        if (gamesToRender.length === 0) {
            gameGrid.innerHTML = '<div class="no-results"><i class="fas fa-search"></i><p>没有找到匹配的游戏</p></div>';
            return;
        }

        gamesToRender.forEach(game => {
            const gameCard = this.createGameCard(game);
            gameGrid.appendChild(gameCard);
        });
    }

    createGameCard(game) {
        const card = document.createElement('div');
        card.className = 'game-card';
        card.dataset.gameId = game.id;

        const isFavorite = this.favorites.includes(game.id);

        // Construct image path
        const imagePath = `images/${game.id}-${game.titleEn.replace(/\s+/g, '_')}.png`;

        card.innerHTML = `
            <button class="favorite-btn ${isFavorite ? 'active' : ''}" data-id="${game.id}">
                <i class="fas fa-star"></i>
            </button>
            <div class="game-cover">
                <img src="${imagePath}" alt="${game.title}" onerror="this.parentElement.classList.add('fallback');this.remove();">
                <i class="fas ${game.icon}" style="display:none;"></i>
            </div>
            <div class="game-info">
                <h3 class="game-title">${game.title}</h3>
                <div class="game-meta">
                    <span class="game-tag">${game.year}</span>
                    <span class="game-tag">${genreNames[game.genre]}</span>
                </div>
                <div class="game-rating">
                    <i class="fas fa-star"></i>
                    <span>${game.rating.toFixed(1)}</span>
                </div>
            </div>
        `;

        // Card click event
        card.addEventListener('click', (e) => {
            if (!e.target.closest('.favorite-btn')) {
                this.showGameModal(game);
            }
        });

        // Favorite button event
        const favoriteBtn = card.querySelector('.favorite-btn');
        favoriteBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.toggleFavorite(game.id);
        });

        return card;
    }

    adjustColor(color, amount) {
        const num = parseInt(color.replace('#', ''), 16);
        const r = Math.max(0, Math.min(255, (num >> 16) + amount));
        const g = Math.max(0, Math.min(255, ((num >> 8) & 0x00FF) + amount));
        const b = Math.max(0, Math.min(255, (num & 0x0000FF) + amount));
        return `#${((r << 16) | (g << 8) | b).toString(16).padStart(6, '0')}`;
    }

    // Show game detail modal
    showGameModal(game) {
        this.currentGame = game;

        const modal = document.getElementById('gameModal');
        document.getElementById('modalTitle').textContent = game.title;
        document.getElementById('modalYear').textContent = game.year + '年';
        document.getElementById('modalGenre').textContent = genreNames[game.genre];
        document.getElementById('modalPublisher').textContent = game.publisher;
        document.getElementById('modalDescription').textContent = game.description;
        document.getElementById('modalRating').textContent = game.rating.toFixed(1);

        modal.classList.add('active');
    }

    // Setup event listeners
    setupEventListeners() {
        // Close modal
        document.querySelector('.close-btn').addEventListener('click', () => {
            document.getElementById('gameModal').classList.remove('active');
        });

        // Play button
        document.getElementById('playBtn').addEventListener('click', () => {
            if (this.currentGame) {
                this.startGame(this.currentGame);
            }
        });

        // Filter buttons
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.filterGames(btn.dataset.filter);
            });
        });

        // Search input
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', (e) => {
            this.searchGames(e.target.value);
        });

        // Favorites button
        document.getElementById('favoritesBtn').addEventListener('click', () => {
            this.showFavorites();
        });

        // Recent button
        document.getElementById('recentBtn').addEventListener('click', () => {
            this.showRecentlyPlayed();
        });

        // Close emulator modal
        document.querySelector('.close-emu-btn').addEventListener('click', () => {
            this.closeEmulator();
        });

        // Emulator controls
        document.getElementById('pauseBtn').addEventListener('click', () => {
            this.togglePause();
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            this.resetGame();
        });

        document.getElementById('saveBtn').addEventListener('click', () => {
            this.saveState();
        });

        document.getElementById('loadBtn').addEventListener('click', () => {
            this.loadState();
        });

        document.getElementById('muteBtn').addEventListener('click', () => {
            this.toggleMute();
        });

        // Close modals on outside click
        window.addEventListener('click', (e) => {
            const gameModal = document.getElementById('gameModal');
            const emuModal = document.getElementById('emulatorModal');

            if (e.target === gameModal) {
                gameModal.classList.remove('active');
            }
            if (e.target === emuModal) {
                this.closeEmulator();
            }
        });

        // Keyboard controls
        this.setupKeyboardControls();
    }

    // Filter games by genre
    filterGames(genre) {
        this.currentFilter = genre;
        if (genre === 'all') {
            this.renderGames(this.games);
        } else {
            const filtered = this.games.filter(game => game.genre === genre);
            this.renderGames(filtered);
        }
    }

    // Search games
    searchGames(query) {
        if (!query.trim()) {
            this.filterGames(this.currentFilter);
            return;
        }

        const searchTerm = query.toLowerCase();
        const filtered = this.games.filter(game =>
            game.title.toLowerCase().includes(searchTerm) ||
            game.titleEn.toLowerCase().includes(searchTerm) ||
            game.description.toLowerCase().includes(searchTerm)
        );

        this.renderGames(filtered);
    }

    // Show favorites
    showFavorites() {
        const favoriteGames = this.games.filter(game => this.favorites.includes(game.id));
        this.renderGames(favoriteGames);

        // Update UI
        document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    }

    // Show recently played
    showRecentlyPlayed() {
        const recentGames = this.games.filter(game =>
            this.recentlyPlayed.some(item => item.id === game.id)
        ).sort((a, b) => {
            const aTime = this.recentlyPlayed.find(item => item.id === a.id)?.timestamp || 0;
            const bTime = this.recentlyPlayed.find(item => item.id === b.id)?.timestamp || 0;
            return bTime - aTime;
        });

        this.renderGames(recentGames);

        // Update UI
        document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    }

    // Toggle favorite
    toggleFavorite(gameId) {
        const index = this.favorites.indexOf(gameId);
        if (index > -1) {
            this.favorites.splice(index, 1);
        } else {
            this.favorites.push(gameId);
        }

        localStorage.setItem('nes_favorites', JSON.stringify(this.favorites));
        this.updateStats();

        // Re-render current view
        this.refreshCurrentView();
    }

    refreshCurrentView() {
        const searchInput = document.getElementById('searchInput');
        if (searchInput.value.trim()) {
            this.searchGames(searchInput.value);
        } else {
            this.filterGames(this.currentFilter);
        }
    }

    // Update stats
    updateStats() {
        document.getElementById('totalGames').textContent = this.games.length + '+';
        document.getElementById('totalPlayed').textContent = this.recentlyPlayed.length;
        document.getElementById('totalFavorites').textContent = this.favorites.length;
    }

    // Load from storage
    loadFromStorage() {
        this.updateStats();
    }

    // Start game (placeholder for emulator integration)
    startGame(game) {
        // Close game modal
        document.getElementById('gameModal').classList.remove('active');

        // Show emulator modal
        const emuModal = document.getElementById('emulatorModal');
        document.getElementById('emuTitle').textContent = `正在运行：${game.title}`;
        emuModal.classList.add('active');

        // Add to recently played
        this.addToRecentlyPlayed(game.id);

        // Initialize emulator (placeholder)
        this.initEmulator(game);

        // Show notification
        this.showNotification(`正在加载 ${game.title}...`);
    }

    addToRecentlyPlayed(gameId) {
        // Remove if already exists
        const index = this.recentlyPlayed.findIndex(item => item.id === gameId);
        if (index > -1) {
            this.recentlyPlayed.splice(index, 1);
        }

        // Add to front
        this.recentlyPlayed.unshift({
            id: gameId,
            timestamp: Date.now()
        });

        // Keep only last 20
        this.recentlyPlayed = this.recentlyPlayed.slice(0, 20);

        localStorage.setItem('nes_recent', JSON.stringify(this.recentlyPlayed));
        this.updateStats();
    }

    // Initialize emulator with JSNES
    async initEmulator(game) {
        const canvas = document.getElementById('nesCanvas');
        const ctx = canvas.getContext('2d');

        // Set canvas size
        canvas.width = 256;
        canvas.height = 240;

        // Show loading
        ctx.fillStyle = '#000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#fff';
        ctx.font = '16px monospace';
        ctx.textAlign = 'center';
        ctx.fillText('正在加载模拟器...', canvas.width / 2, canvas.height / 2);

        try {
            // Initialize emulator
            if (!window.nesEmulator) {
                window.nesEmulator = new NESEmulator(canvas);
                const initialized = await window.nesEmulator.init();
                if (!initialized) {
                    throw new Error('模拟器初始化失败');
                }
            }

            // Try to load ROM
            const romPath = `roms/${game.id}-${game.titleEn.replace(/\s+/g, '_')}.nes`;

            try {
                const response = await fetch(romPath);

                if (!response.ok) {
                    throw new Error('ROM not found');
                }

                const romData = await response.arrayBuffer();
                const romArray = new Uint8Array(romData);

                // Load and run ROM
                window.nesEmulator.loadROM(romArray);
                this.showNotification(`${game.title} 开始运行！`);

            } catch (romError) {
                // ROM not found - show demo message
                ctx.fillStyle = '#000';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = '#fff';
                ctx.font = '14px monospace';
                ctx.textAlign = 'center';
                ctx.fillText('ROM文件未找到', canvas.width / 2, canvas.height / 2 - 20);
                ctx.font = '12px monospace';
                ctx.fillText(`需要: ${romPath}`, canvas.width / 2, canvas.height / 2 + 10);
                ctx.fillText('请查看 roms/README.md', canvas.width / 2, canvas.height / 2 + 30);

                this.showNotification('ROM文件未找到');
                console.log('ROM not found:', romPath);
            }

        } catch (error) {
            ctx.fillStyle = '#000';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#f00';
            ctx.font = '14px monospace';
            ctx.textAlign = 'center';
            ctx.fillText('模拟器错误:', canvas.width / 2, canvas.height / 2 - 10);
            ctx.fillStyle = '#fff';
            ctx.font = '12px monospace';
            ctx.fillText(error.message, canvas.width / 2, canvas.height / 2 + 20);

            this.showNotification('模拟器初始化失败');
            console.error('Emulator error:', error);
        }
    }

    // Emulator controls
    togglePause() {
        this.isPaused = !this.isPaused;
        const btn = document.getElementById('pauseBtn');
        btn.innerHTML = this.isPaused ?
            '<i class="fas fa-play"></i> 继续' :
            '<i class="fas fa-pause"></i> 暂停';

        if (window.nesEmulator) {
            if (this.isPaused) {
                window.nesEmulator.pause();
            } else {
                window.nesEmulator.resume();
            }
        }

        this.showNotification(this.isPaused ? '游戏已暂停' : '游戏继续');
    }

    resetGame() {
        if (window.nesEmulator && this.currentGame) {
            window.nesEmulator.reset();
            this.showNotification('游戏已重置');
        }
    }

    saveState() {
        if (window.nesEmulator) {
            const saveSlot = this.currentGame ? this.currentGame.id : 1;
            if (window.nesEmulator.saveState(saveSlot)) {
                this.showNotification('游戏状态已保存');
            } else {
                this.showNotification('保存失败');
            }
        }
    }

    loadState() {
        if (window.nesEmulator) {
            const saveSlot = this.currentGame ? this.currentGame.id : 1;
            if (window.nesEmulator.loadState(saveSlot)) {
                this.showNotification('游戏状态已加载');
            } else {
                this.showNotification('没有找到存档');
            }
        }
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        const btn = document.getElementById('muteBtn');
        btn.innerHTML = this.isMuted ?
            '<i class="fas fa-volume-mute"></i>' :
            '<i class="fas fa-volume-up"></i>';

        this.showNotification(this.isMuted ? '静音' : '取消静音');
    }

    closeEmulator() {
        const emuModal = document.getElementById('emulatorModal');
        emuModal.classList.remove('active');
        this.isPaused = false;
        this.currentGame = null;
    }

    // Setup keyboard controls
    setupKeyboardControls() {
        // Support both key and code for better compatibility
        const keyMap = {
            // Arrow keys
            'ArrowUp': 'up', 'arrowup': 'up', 'up': 'up',
            'ArrowDown': 'down', 'arrowdown': 'down', 'down': 'down',
            'ArrowLeft': 'left', 'arrowleft': 'left', 'left': 'left',
            'ArrowRight': 'right', 'arrowright': 'right', 'right': 'right',
            // Action buttons
            'z': 'a', 'Z': 'a', 'KeyZ': 'a',
            'x': 'b', 'X': 'b', 'KeyX': 'b',
            // Control buttons
            'Enter': 'start', 'enter': 'start',
            'Shift': 'select', 'ShiftLeft': 'select', 'ShiftRight': 'select'
        };

        document.addEventListener('keydown', (e) => {
            if (!document.getElementById('emulatorModal').classList.contains('active')) {
                return;
            }

            // Check both e.key and e.code
            const key = e.key || e.code || '';
            const action = keyMap[key];

            if (action) {
                e.preventDefault();
                e.stopPropagation();
                console.log('Key pressed:', key, '-> Action:', action);
                this.handleNESInput(action, true);
            }
        });

        document.addEventListener('keyup', (e) => {
            if (!document.getElementById('emulatorModal').classList.contains('active')) {
                return;
            }

            // Check both e.key and e.code
            const key = e.key || e.code || '';
            const action = keyMap[key];

            if (action) {
                e.preventDefault();
                e.stopPropagation();
                this.handleNESInput(action, false);
            }
        });
    }

    handleNESInput(button, pressed) {
        if (window.nesEmulator && typeof jsnes !== 'undefined') {
            const buttonMap = {
                'up': jsnes.Controller.BUTTON_UP,
                'down': jsnes.Controller.BUTTON_DOWN,
                'left': jsnes.Controller.BUTTON_LEFT,
                'right': jsnes.Controller.BUTTON_RIGHT,
                'a': jsnes.Controller.BUTTON_A,
                'b': jsnes.Controller.BUTTON_B,
                'start': jsnes.Controller.BUTTON_START,
                'select': jsnes.Controller.BUTTON_SELECT
            };

            const nesButton = buttonMap[button];
            if (nesButton) {
                if (pressed) {
                    window.nesEmulator.buttonDown(nesButton);
                } else {
                    window.nesEmulator.buttonUp(nesButton);
                }
            }
        }
    }

    // Show notification
    showNotification(message) {
        // Remove existing notification
        const existing = document.querySelector('.nes-notification');
        if (existing) {
            existing.remove();
        }

        // Create notification
        const notification = document.createElement('div');
        notification.className = 'nes-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #E60012, #C4000F);
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            z-index: 10000;
            animation: slideIn 0.3s ease, fadeOut 0.3s ease 2.7s;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        `;

        document.body.appendChild(notification);

        // Add animations
        if (!document.querySelector('#nes-animations')) {
            const style = document.createElement('style');
            style.id = 'nes-animations';
            style.textContent = `
                @keyframes slideIn {
                    from { transform: translateX(100%); opacity: 0; }
                    to { transform: translateX(0); opacity: 1; }
                }
                @keyframes fadeOut {
                    from { opacity: 1; }
                    to { opacity: 0; }
                }
            `;
            document.head.appendChild(style);
        }

        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
}

// Initialize app when DOM is loaded
function initApp() {
    if (!window.nesGameStation) {
        window.nesGameStation = new NESGameStation();
        console.log('✅ NES Game Station 初始化成功');
    }
}

// 支持动态加载和普通加载
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    // DOM 已经加载完成（动态加载的情况）
    initApp();
}
