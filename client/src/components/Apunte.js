function Apunte(props) {
	return (
		<div className="card">
			<div className="card-header">{props.titulo}</div>
			<div className="card-body">
				<p className="card-text">{props.contenido}</p>
				<div
					className="btn btn-warning"
					data-bs-toggle="modal"
					data-bs-target="#ApunteModal"
					onClick={(e) => props.setNote(props.titulo, props.contenido)}
				>
					Ver Apunte
				</div>
			</div>
		</div>
	);
}

export default Apunte;
