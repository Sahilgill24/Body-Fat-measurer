const dragItems = document.querySelectorAll('.drag-item');
const dropZone = document.querySelector('#dropzone');

dragItems.forEach(dragItem => {
  dragItem.addEventListener('dragstart', () => {
    dragItem.classList.add('dragging');
  });

  dragItem.addEventListener('dragend', () => {
    dragItem.classList.remove('dragging');
  });
});

dropZone.addEventListener('dragover', (event) => {
  event.preventDefault();
});

dropZone.addEventListener('drop', (event) => {
  event.preventDefault();
  const droppedItem = document.querySelector('.dragging');
  dropZone.appendChild(droppedItem);
});
