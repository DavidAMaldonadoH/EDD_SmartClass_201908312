import { useState } from 'react';
import { useHistory } from 'react-router';

import NavBar from './NavBar';
import Input from './Input';
import userIcon from '../icons/user-solid.svg';

function Login(props) {
	const history = useHistory();
	const [user, setUser] = useState({ userName: '', password: '' });

	const fetchUser = async (carnet, password) => {
		const res = await fetch(`http://localhost:3000/user/${carnet}/${password}`);
		return await res.json();
	};

	const onChange = (name, value) => {
		if (name === 'Usuario') {
			setUser({ ...user, userName: value });
		} else {
			setUser({ ...user, password: value });
		}
	};

	const onSubmit = (e) => {
		e.preventDefault();
		if (user.userName === 'admin') {
			if (user.password !== 'admin') {
				alert('contraseña incorrecta!');
			} else {
				props.isLoggedIn(true);
				const account = JSON.stringify(user);
				localStorage.setItem('account', account);
				history.push('/dashboard');
			}
		} else {
			fetchUser(user.userName, user.password).then((value) => {
				if (value.msg === 'log') {
					props.account({
						carnet: value.carnet,
						DPI: value.DPI,
						nombre: value.nombre,
						carrera: value.carrera,
						correo: value.correo,
						password: value.password,
						creditos: value.creditos,
						edad: value.edad,
					});
					props.isLoggedIn(true);
					const account = JSON.stringify(user);
					localStorage.setItem('account', account);
					history.push('/dashboard');
				} else {
					alert(value.msg);
				}
			});
		}
	};

	return (
		<>
			<NavBar />
			<div className="container d-flex justify-content-center align-items-center">
				<div className="card text-center" style={{ minWidth: '30%' }}>
					<h5 className="card-header">Login</h5>
					<div className="mt-4">
						<img
							src={userIcon}
							className="card-img-top"
							alt="user"
							style={{ height: '100px', width: '100px' }}
						/>
					</div>
					<div className="card-body">
						<form onSubmit={onSubmit}>
							<Input texto="Usuario" tipo="text" onChange={onChange} />
							<Input texto="Password" tipo="password" onChange={onChange} />
							<button className="w-100 btn btn-primary" type="submit">
								Sign in
							</button>
							<p className="mt-5 mb-3 text-muted">&copy;2021</p>
						</form>
					</div>
				</div>
			</div>
		</>
	);
}

export default Login;
