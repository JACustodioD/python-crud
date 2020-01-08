import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','Company','Email','Position']
clients = []

def _initialize_clients_from_storage():
	with open(CLIENT_TABLE,mode='r') as f:
		reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)


def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name,mode='w') as f:
		writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

		os.remove(CLIENT_TABLE)
		os.rename(tmp_table_name,CLIENT_TABLE)



def create_client(client):
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print('Client is already is in the client\'s list')

def list_clients():
	for idx,client in enumerate(clients):
		print('{uid} | {name} | {Company} | {Email} | {Position}'.format(
			uid = idx,
			name = client['name'],
			Company = client['Company'],
			Email = client['Email'],
			Position = client['Position']
			))

def update_client(updated_client,updated_client_id):
	global clients

	if len(clients) < int(updated_client_id):
		print('This user not exist')
	else:
		clients[int(updated_client_id)] = updated_client


def delete_client(updated_client_id):
	global clients

	if len(clients) < int(updated_client_id):
		print('This user not exist')
	else:
		clients.pop(int(updated_client_id))
		print('this client was deleted')


def search_client(updated_client_id):
	global clients

	if len(clients) < int(updated_client_id):
		return False
	else:
		for idx,client in enumerate(clients):
			if idx == int(updated_client_id):
				return True
			else:
				continue




def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*'*50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[L]ist clients')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')

def _get_client_field(field_name):
	field = None

	while not field:
		field = input('What is the client {}? '.format(field_name))

	return field

def _get_client_name():
	client_name = None 

	while not client_name:
		client_name = input('What is the client name? ')
		if client_name == 'exit':
			client_name = None
			break
	if not client_name:
		sys.exit()

	return client_name


if __name__ == '__main__':
	_initialize_clients_from_storage()
	_print_welcome()
	command = input()
	command = command.upper()

	if command == 'C':
		client = {
			'name': _get_client_field('name'),
			'Company': _get_client_field('Company'),
			'Email': _get_client_field('Email'),
			'Position': _get_client_field('Position')
		}
		create_client(client)

	elif command == 'U':
		updated_client = {
			'name': _get_client_field('name'),
			'Company': _get_client_field('Company'),
			'Email': _get_client_field('Email'),
			'Position': _get_client_field('Position')
		}
		updated_client_id = input('What is the updated client id? ')
		update_client(updated_client,updated_client_id)

	elif command == 'L':
		list_clients()
	elif command == 'D':
		updated_client_id = _get_client_field('id')
		delete_client(updated_client_id)
	elif command == 'S':
		updated_client_id = _get_client_field('id')
		found = search_client(updated_client_id)

		if found:
			print('The client is in the client\'s list')
		else:
			print('The client whit the id: {} is not in out client\'s list'.format(updated_client_id))
	else:
		print('Invalid command')

	_save_clients_to_storage()