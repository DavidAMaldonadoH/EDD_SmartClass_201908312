function ModalApunte(props) {
	return (
		<div
			className="modal fade"
			id="ApunteModal"
			tabIndex={-1}
			aria-labelledby="ApunteModalLabel"
			aria-hidden="true"
		>
			<div className="modal-dialog modal-dialog-scrollable modal-xl">
				<div className="modal-content">
					<div className="modal-header">
						<h5 className="modal-title" id="ApunteModalLabel">
							{props.note.titulo}
						</h5>
						<button
							type="button"
							className="btn-close"
							data-bs-dismiss="modal"
							aria-label="Close"
						></button>
					</div>
					<div className="modal-body">
						<div>{props.note.contenido}</div>
					</div>
					<div className="modal-footer">
						<button type="button" className="btn btn-danger" data-bs-dismiss="modal">
							Close
						</button>
					</div>
				</div>
			</div>
		</div>
	);
}

export default ModalApunte;
