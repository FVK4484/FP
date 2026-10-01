package fp.tipos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import fp.utiles.Checkers;

public class Pedido implements Comparable<Pedido>{
	private List<Producto> productos;
	private LocalDate fechaPedido;
	private LocalDate fechaEntrega;
	private Boolean pagado;
	private LugarCompra lugarCompra;
	
	public Pedido(List<Producto> productos, LocalDate fechaPedido, Boolean pagado, LugarCompra lugarCompra) {
		Checkers.check("La lista no puede estar vacía.", productos.size() > 0);
		this.productos = new ArrayList<>(productos);
		this.fechaPedido = fechaPedido;
		this.fechaEntrega = null;
		this.pagado = pagado;
		this.lugarCompra = lugarCompra;
	}

	public List<Producto> getProductos() {
		return new ArrayList<>(productos);
	}

	public void setProductos(List<Producto> productos) {
		this.productos = productos;
	}

	public LocalDate getFechaPedido() {
		return fechaPedido;
	}

	public void setFechaPedido(LocalDate fechaPedido) {
		this.fechaPedido = fechaPedido;
	}

	public LocalDate getFechaEntrega() {
		return fechaEntrega;
	}

	public void setFechaEntrega(LocalDate fechaEntrega) {
		this.fechaEntrega = fechaEntrega;
	}

	public Boolean getPagado() {
		return pagado;
	}

	public void setPagado(Boolean pagado) {
		this.pagado = pagado;
	}

	public LugarCompra getLugarCompra() {
		return lugarCompra;
	}
	
	public Integer getNumDiasEntrega() {
		return fechaPedido.until(fechaEntrega).getDays();
	}
	
	public String toString() {
		return "Pedido[productos=" + productos + ", fechaPedido=" + fechaPedido + ", fechaEntrega=" + fechaEntrega
				+ ", pagado=" + pagado + ", lugarCompra=" + lugarCompra + "]";
	}

	public int hashCode() {
		return Objects.hash(fechaEntrega, fechaPedido, lugarCompra, pagado, productos);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pedido other = (Pedido) obj;
		return Objects.equals(fechaEntrega, other.fechaEntrega) && Objects.equals(fechaPedido, other.fechaPedido)
				&& lugarCompra == other.lugarCompra && Objects.equals(pagado, other.pagado)
				&& Objects.equals(productos, other.productos);
	}

	public int compareTo(Pedido p) {
		Integer res = getFechaPedido().compareTo(p.getFechaPedido());
		if (res == 0) {
			Integer uno = getProductos().size();
			Integer dos = p.getProductos().size();
			res = uno.compareTo(dos);
		}
		return res;
	}
	
}
