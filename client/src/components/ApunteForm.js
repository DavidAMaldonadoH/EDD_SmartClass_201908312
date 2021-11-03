function ApunteForm(props) {
	return (
		<div className="m-4">
			<div className="mb-3 row">
				<label htmlFor="carnetApunte" className="col-sm-2 col-form-label">
					Carnet
				</label>
				<div className="col-sm-10">
					<input
						type="text"
						className="form-control"
						id="carnetApunte"
						placeholder={props.account.carnet}
						readOnly
					/>
				</div>
			</div>
			<div className="mb-3 row">
				<label htmlFor="tituloApunte" className="col-sm-2 col-form-label">
					Titulo
				</label>
				<div className="col-sm-10">
					<input type="text" className="form-control" id="tituloApunte" placeholder="Apunte 1" />
				</div>
			</div>
			<div>
				<label htmlFor="exampleFormControlTextarea1" className="form-label">
					Contenido
				</label>
				<textarea
					className="form-control"
					id="exampleFormControlTextarea1"
					rows={3}
					defaultValue={''}
				/>
			</div>
			<div className="text-end">
				<button type="submit" className="btn btn-primary mt-2">
					Confirm identity
				</button>
			</div>
		</div>
	);
}

export default ApunteForm;
