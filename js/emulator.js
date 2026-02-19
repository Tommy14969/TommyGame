/**
 * JSNES Emulator Integration
 * This file wraps the JSNES library for easy integration
 */

class NESEmulator {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.nes = null;
        this.ui = null;
        this.running = false;
        this.paused = false;
        this.currentROM = null;

        // Initialize canvas
        this.canvas.width = 256;
        this.canvas.height = 240;

        // Image data for rendering
        this.imageData = this.ctx.createImageData(256, 240);

        // Frame buffer
        this.buffer = new Uint8Array(256 * 240 * 4);
    }

    async init() {
        try {
            // Load JSNES library
            if (typeof jsnes === 'undefined') {
                throw new Error('JSNES library not loaded. Please include jsnes.js');
            }

            // Initialize NES
            this.nes = new jsnes.NES({
                onFrame: this.onFrame.bind(this),
                onAudioSample: this.onAudioSample.bind(this),
                sampleRate: 44100
            });

            console.log('NES Emulator initialized');
            return true;
        } catch (error) {
            console.error('Failed to initialize NES emulator:', error);
            this.showError('模拟器初始化失败');
            return false;
        }
    }

    loadROM(romData) {
        try {
            // Convert Uint8Array to string for JSNES compatibility
            let romString;
            if (romData instanceof Uint8Array) {
                romString = '';
                for (let i = 0; i < romData.length; i++) {
                    romString += String.fromCharCode(romData[i]);
                }
            } else if (typeof romData === 'string') {
                romString = romData;
            } else {
                throw new Error('Invalid ROM data type');
            }

            this.nes.loadROM(romString);
            this.currentROM = romData;
            this.running = true;
            this.paused = false;
            this.startFrame();
            console.log('ROM loaded successfully');
            return true;
        } catch (error) {
            console.error('Failed to load ROM:', error);
            const errorMsg = error.message || '';

            // Check for mapper error
            if (errorMsg.includes('mapper') || errorMsg.includes('Mapper')) {
                this.showError('❌ Mapper不支持\n\n此游戏使用了JSNES不支持的Mapper。\n\n请尝试其他版本的ROM。');
            } else {
                this.showError('ROM加载失败: ' + errorMsg);
            }
            return false;
        }
    }

    onFrame(buffer) {
        // Render frame to canvas
        const imageData = this.ctx.createImageData(256, 240);
        const data = imageData.data;

        for (let i = 0; i < buffer.length; i++) {
            const pixel = buffer[i];
            const r = ((pixel >> 16) & 0xFF);
            const g = ((pixel >> 8) & 0xFF);
            const b = (pixel & 0xFF);

            const index = i * 4;
            data[index] = r;
            data[index + 1] = g;
            data[index + 2] = b;
            data[index + 3] = 255;
        }

        this.ctx.putImageData(imageData, 0, 0);
    }

    onAudioSample(left, right) {
        // Audio handling (to be implemented)
        // This would connect to Web Audio API
    }

    startFrame() {
        if (this.running && !this.paused) {
            this.nes.frame();
            requestAnimationFrame(this.startFrame.bind(this));
        }
    }

    buttonDown(button) {
        console.log('[Emulator] buttonDown called:', button, 'running:', this.running, 'nes:', !!this.nes);
        if (this.nes && this.running) {
            this.nes.buttonDown(1, button);
            console.log('[Emulator] Button DOWN sent to JSNES:', button);
        } else {
            console.error('[Emulator] Cannot press button - NES not running or initialized');
        }
    }

    buttonUp(button) {
        console.log('[Emulator] buttonUp called:', button);
        if (this.nes && this.running) {
            this.nes.buttonUp(1, button);
            console.log('[Emulator] Button UP sent to JSNES:', button);
        }
    }

    pause() {
        this.paused = true;
    }

    resume() {
        this.paused = false;
        this.startFrame();
    }

    reset() {
        if (this.nes && this.currentROM) {
            this.nes.reloadROM();
            this.paused = false;
            this.startFrame();
        }
    }

    saveState(slot) {
        // Save game state to localStorage
        try {
            const state = this.nes.toJSON();
            const saveKey = `nes_save_${slot}`;
            localStorage.setItem(saveKey, JSON.stringify(state));
            return true;
        } catch (error) {
            console.error('Failed to save state:', error);
            return false;
        }
    }

    loadState(slot) {
        // Load game state from localStorage
        try {
            const saveKey = `nes_save_${slot}`;
            const stateData = localStorage.getItem(saveKey);
            if (stateData) {
                const state = JSON.parse(stateData);
                this.nes.fromJSON(state);
                return true;
            }
            return false;
        } catch (error) {
            console.error('Failed to load state:', error);
            return false;
        }
    }

    exportState(slot, gameName) {
        // Export game state as a downloadable file
        try {
            const state = this.nes.toJSON();
            const saveData = {
                version: '1.0',
                gameName: gameName,
                gameId: slot,
                timestamp: new Date().toISOString(),
                state: state
            };

            // Create blob and download link
            const blob = new Blob([JSON.stringify(saveData, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${gameName}_save_${new Date().toISOString().slice(0, 10)}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            return true;
        } catch (error) {
            console.error('Failed to export state:', error);
            return false;
        }
    }

    async importState(fileData) {
        // Import game state from a file
        try {
            const saveData = JSON.parse(fileData);

            // Validate save data format
            if (!saveData.state) {
                throw new Error('Invalid save file format');
            }

            // Load the state
            this.nes.fromJSON(saveData.state);

            return {
                success: true,
                gameName: saveData.gameName,
                timestamp: saveData.timestamp
            };
        } catch (error) {
            console.error('Failed to import state:', error);
            return { success: false, error: error.message };
        }
    }

    stop() {
        this.running = false;
        this.paused = false;
    }

    showError(message) {
        this.ctx.fillStyle = '#000';
        this.ctx.fillRect(0, 0, 256, 240);

        this.ctx.fillStyle = '#fff';
        this.ctx.font = '16px monospace';
        this.ctx.textAlign = 'center';
        this.ctx.fillText(message, 128, 120);
    }

    showLoading() {
        this.ctx.fillStyle = '#000';
        this.ctx.fillRect(0, 0, 256, 240);

        this.ctx.fillStyle = '#fff';
        this.ctx.font = '16px monospace';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('加载中...', 128, 120);
    }
}

// Export for use in app.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { NESEmulator };
}
