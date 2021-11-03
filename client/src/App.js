import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import { useState, useEffect } from 'react';

import Login from './components/Login';
import Register from './components/Register';
import AdminPage from './components/AdminPage';
import UserPage from './components/UserPage';
import ApuntesPage from './components/ApuntesPage';

function App() {
	const [loggedIn, setLoggedIn] = useState(false);
	const [account, setAccount] = useState({
		carnet: '',
		DPI: '',
		nombre: '',
		carrera: '',
		correo: '',
		password: '',
		creditos: 0,
		edad: 0,
	});

	let user = JSON.parse(localStorage.getItem('account'));

	useEffect(() => {
		let account = localStorage.getItem('account');
		if (account) {
			setLoggedIn(true);
		} else {
			setLoggedIn(false);
		}
	}, []);

	const logOut = () => {
		localStorage.removeItem('account');
		setLoggedIn(false);
	};

	return (
		<Router>
			<Route path="/" exact>
				{loggedIn ? <Redirect to="/dashboard" /> : <Redirect to="/login" />}
			</Route>
			<Route
				path="/login"
				render={(props) => <Login isLoggedIn={setLoggedIn} account={setAccount} />}
			/>
			<Route path="/register" component={Register} />
			<Route path="/dashboard">
				{user?.userName === 'admin' ? (
					<Redirect to="/dashboard/admin" />
				) : (
					<Redirect to="/dashboard/user" />
				)}
			</Route>
			<Route path="/dashboard/admin" render={(props) => <AdminPage onLogOut={logOut} />} />
			<Route
				path="/dashboard/user"
				render={(props) => <UserPage onLogOut={logOut} account={account} />}
			/>
			<Route
				path="/dashboard/user/apuntes"
				render={(props) => <ApuntesPage onLogOut={logOut} account={account} />}
			/>
		</Router>
	);
}

export default App;
