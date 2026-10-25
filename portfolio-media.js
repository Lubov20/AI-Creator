const VIDEO_URL = 'https://pub-3feacf8318dc4eff90d2b4327613b5ef.r2.dev/videos/1017(1).mp4';

export function createPortfolioMedia({projects, covers, textures, getState}) {
  const project = projects[0];
  project.type = 'motion';
  project.media = {kind: 'video', url: VIDEO_URL};
  const video = document.createElement('video');
  video.crossOrigin = 'anonymous';
  video.preload = 'metadata';
  video.muted = true;
  video.loop = true;
  video.playsInline = true;
  video.hidden = true;
  video.src = VIDEO_URL;
  document.body.append(video);

  const canvas = covers[0], context = canvas.getContext('2d');
  let active = null, wanted = null, userPaused = false, userStarted = false;
  let lastFrame = -1, failed = false;
  const info = document.querySelector('.project-info');
  const type = info.querySelector('.project-type');
  const description = info.querySelector('.project-description');
  const summary = info.querySelector('p:not(.project-type):not(.project-description)');
  const original = [type.innerHTML, summary.innerHTML, description.innerHTML];
  const controls = document.createElement('div');
  controls.className = 'portfolio-media-controls';
  controls.hidden = true;
  controls.innerHTML = '<div><button type="button" data-play aria-label="Воспроизвести видео">Смотреть</button><button type="button" data-sound aria-label="Включить звук">Звук: выкл</button></div><input type="range" min="0" max="1" step="0.1" value="0" aria-label="Позиция видео"><small role="status" aria-live="polite"></small>';
  info.insertBefore(controls, document.querySelector('#project-close'));
  const play = controls.querySelector('[data-play]');
  const sound = controls.querySelector('[data-sound]');
  const seek = controls.querySelector('input');
  const status = controls.querySelector('small');
  const style = document.createElement('style');
  style.textContent = '.portfolio-media-controls{pointer-events:auto;margin:18px 0;max-width:230px}.portfolio-media-controls[hidden]{display:none}.portfolio-media-controls>div{display:flex;gap:20px}.portfolio-media-controls button{font-size:9px!important;margin:0!important}.portfolio-media-controls input{display:block;width:100%;margin:14px 0;accent-color:#df75ba;cursor:pointer}.portfolio-media-controls small{display:block;font-size:8px;line-height:1.5;color:#b8c9c5}';
  document.head.append(style);

  async function start() {
    try { await video.play(); status.textContent = ''; }
    catch { if (active === 0) status.textContent = 'Нажмите «Смотреть», чтобы запустить видео.'; }
  }
  play.onclick = () => {
    userStarted = true;
    if (video.paused) { userPaused = false; wanted = true; start(); }
    else { userPaused = true; wanted = false; video.pause(); }
  };
  sound.onclick = () => {
    video.muted = !video.muted;
    sound.textContent = video.muted ? 'Звук: выкл' : 'Звук: вкл';
    sound.setAttribute('aria-label', video.muted ? 'Включить звук' : 'Выключить звук');
    if (!userPaused) { userStarted = true; wanted = true; start(); }
  };
  seek.oninput = () => {
    if (Number.isFinite(video.duration)) { video.currentTime = Number(seek.value); lastFrame = -1; }
  };
  video.addEventListener('loadedmetadata', () => {
    seek.max = String(video.duration || 1);
    seek.disabled = !Number.isFinite(video.duration);
  });
  video.addEventListener('error', () => {
    failed = true;
    status.textContent = 'Видео временно недоступно. Попробуйте обновить страницу.';
    play.disabled = sound.disabled = seek.disabled = true;
    console.warn('LV portfolio video could not load', video.error?.code);
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) { video.pause(); wanted = null; }
  });

  function tick() {
    const state = getState();
    const focus = Math.max(0, Math.min(1, (state.phase - .25) / .52)) * 5;
    const showing = state.projectOpen ? active === 0 : state.phase > .19 && state.phase < .86 && focus < 1.8;
    const shouldPlay = showing && !document.hidden && !userPaused && (!state.reduced || userStarted) && !failed;
    if (wanted !== shouldPlay) {
      wanted = shouldPlay;
      if (wanted) start(); else video.pause();
    }
    if (video.readyState >= 2 && lastFrame !== video.currentTime) {
      const scale = Math.min(canvas.width / video.videoWidth, canvas.height / video.videoHeight);
      const width = video.videoWidth * scale, height = video.videoHeight * scale;
      context.fillStyle = '#080e10';
      context.fillRect(0, 0, canvas.width, canvas.height);
      context.drawImage(video, (canvas.width - width) / 2, (canvas.height - height) / 2, width, height);
      textures[0].needsUpdate = true;
      lastFrame = video.currentTime;
      project.mediaReady = true;
    }
    if (state.world) state.world.cards[0].material.uniforms.realMedia.value = project.mediaReady ? 1 : 0;
    if (state.projectOpen && active === 0) {
      if (state.detail) state.detail.u.realMedia.value = project.mediaReady ? 1 : 0;
      play.textContent = video.paused ? 'Смотреть' : 'Пауза';
      play.setAttribute('aria-label', video.paused ? 'Воспроизвести видео' : 'Приостановить видео');
      if (document.activeElement !== seek && Number.isFinite(video.currentTime)) seek.value = String(video.currentTime);
    }
  }
  return {
    tick,
    open(index) {
      active = index;
      wanted = null;
      controls.hidden = index !== 0;
      type.innerHTML = index === 0 ? 'LV / AI-ВИДЕО' : original[0];
      summary.innerHTML = index === 0 ? 'Работа Крайновой Любови.' : original[1];
      description.innerHTML = index === 0 ? 'Видео из авторского портфолио.' : original[2];
      const {detail} = getState();
      if (detail) detail.u.realMedia.value = index === 0 && project.mediaReady ? 1 : 0;
      tick();
    },
    close() {
      active = null;
      video.muted = true;
      sound.textContent = 'Звук: выкл';
      sound.setAttribute('aria-label', 'Включить звук');
      userPaused = false;
      wanted = null;
    }
  };
}
