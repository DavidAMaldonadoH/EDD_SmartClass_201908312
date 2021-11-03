import NavBarUser from './NavBarUser';
import UserInfo from './UserInfo';

function UserPage(props) {
	return (
		<>
			<NavBarUser onLogOut={props.onLogOut} />
			<div className="container d-flex">
				<UserInfo account={props.account} />
			</div>
		</>
	);
}

export default UserPage;
