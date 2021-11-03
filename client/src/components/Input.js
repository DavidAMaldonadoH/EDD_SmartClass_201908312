function Input(props) {
	return (
		<div className="form-floating mb-3">
			<input
				type={props.tipo}
				className="form-control"
				id={props.texto + 'Input'}
				name={props.texto}
				placeholder={props.texto}
				onChange={(e) => props.onChange(e.target.name, e.target.value)}
			/>
			<label htmlFor="floatingInput">{props.texto}</label>
		</div>
	);
}

export default Input;
