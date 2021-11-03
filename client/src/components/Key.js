function Key(props) {
	return (
		<div
			className="keyContainer d-flex flex-row justify-content-center w-100"
		>
			<label
				className="text-white text-center fw-bold bg-dark col-sm-2 col-form-label"
				style={{ width: '15%', height: '50px' }}
			>
				Key:
			</label>
			<textarea
				className="form-control"
				style={{ resize: 'none', width: '70%', height: '50px' }}
				readOnly
				value={props.texto}
			></textarea>
			<button className="btn btn-success" type="submit" style={{width: '15%', height: '50px'}} onClick={props.getKey}>
				Generar Key
			</button>
		</div>
	);
}

export default Key;
