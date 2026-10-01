package fp.tipos.test;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import fp.tipos.FactoriaProductos;
import fp.tipos.LugarCompra;
import fp.tipos.Pedido;
import fp.tipos.Producto;

public class TestProductoPedido {

	public static void main(String[] args) {
		
		Producto prod1 = new Producto("Pantalla", 20.0, 50);
		List<Producto> listaProds = new ArrayList<>();
		listaProds.add(prod1);
		System.out.println(prod1);
		
		Pedido pedido1 = new Pedido(listaProds, LocalDate.now(), false, LugarCompra.ONLINE);
		Pedido pedido2 = new Pedido(listaProds, LocalDate.now(), true, LugarCompra.TIENDA);
		Pedido p = new Pedido(listaProds, LocalDate.now(), true, LugarCompra.OTRO);
		System.out.println(pedido1.getFechaPedido());
		pedido1.setPagado(true);
		pedido1.setFechaEntrega(LocalDate.now().plusDays(1));
		System.out.println(pedido1.getFechaEntrega());
		Producto prod2 = FactoriaProductos.parseaProducto("Pantalla;20.0;80");
		System.out.println(prod2);
		
		List<Pedido> pedidos = new ArrayList<>();
		pedidos.add(pedido1);
		pedidos.add(pedido2);
		pedidos.add(p);
		System.out.println(pedidos.getLast());
//		System.out.println(pedidos.get(Integer.valueOf(pedidos.size() - 1)));
		pedidos.remove(2);
		System.out.println(pedidos.get(1).getLugarCompra());
		System.out.println(pedidos.indexOf(p));
	}

}
